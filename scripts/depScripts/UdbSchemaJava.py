import understand
import csv
import sys

Language = "Java"

TypeMap = {
  "File": {
    "Java File",
    "Java File Jar",
  },
  "Method": {
    "Java Abstract Method Default Member",
    "Java Abstract Method Protected Member",
    "Java Abstract Method Public Member",
    "Java Method Constructor Member Default",
    "Java Method Constructor Member Protected",
    "Java Method Constructor Member Private",
    "Java Method Constructor Member Public",
    "Java Final Method Default Member",
    "Java Final Method Private Member",
    "Java Final Method Protected Member",
    "Java Final Method Public Member",
    "Java Method Default Member",
    "Java Method Private Member",
    "Java Method Protected Member",
    "Java Method Public Member",
    "Java Static Final Method Default Member",
    "Java Static Final Method Private Member",
    "Java Static Final Method Protected Member",
    "Java Static Final Method Public Member",
    "Java Static Method Default Member",
    "Java Static Method Private Member",
    "Java Static Method Protected Member",
    "Java Static Method Public Member",
    "Java Static Method Public Main Member",
    "Java Unknown Method Member",
    "Java Unresolved Method",
    "Java Unresolved External Final Method Default Member",
    "Java Unresolved External Final Method Private Member",
    "Java Unresolved External Final Method Protected Member",
    "Java Unresolved External Final Method Public Member",
    "Java Unresolved External Method Default Member",
    "Java Unresolved External Method Private Member",
    "Java Unresolved External Method Protected Member",
    "Java Unresolved External Method Public Member",
    "Java Unresolved External Static Final Method Default Member",
    "Java Unresolved External Static Final Method Private Member",
    "Java Unresolved Extermal Static Final Method Protected Member",
    "Java Unresolved External Static Final Method Public Member",
    "Java Unresolved External Static Method Default Member",
    "Java Unresolved External Static Method Private Member",
    "Java Unresolved External Static Method Protected Member",
    "Java Unresolved External Static Method Public Member",
    "Java Unresolved External Static Method Public Main Member",
  },
  "Package": {
    "Java Package",
    "Java Package Unnamed",
    "Java Unknown Package",
    "Java Unresolved Package",
  },
  "Parameter": {
    "Java Catch Parameter",
    "Java Parameter",
  },
  "Type": {
    "Java Abstract Class Type Default Member",
    "Java Abstract Class Type Private Member",
    "Java Abstract Class Type Protected Member",
    "Java Abstract Class Type Public Member",
    "Java Abstract Enum Type Default Member",
    "Java Abstract Enum Type Private Member",
    "Java Abstract Enum Type Protected Member",
    "Java Abstract Enum Type Public Member",
    "Java Annotation Interface Type Default",
    "Java Annotation Interface Type Private",
    "Java Annotation Interface Type Protected",
    "Java Annotation Interface Type Public",
    "Java Class Type Anonymous Member",
    "Java Class Type Default Member",
    "Java Class Type Private Member",
    "Java Class Type Protected Member",
    "Java Class Type Public Member",
    "Java Enum Class Type Default Member",
    "Java Enum Class Type Private Member",
    "Java Enum Class Type Protected Member",
    "Java Enum Class Type Public Member",
    "Java Final Class Type Default Member",
    "Java Final Class Type Private Member",
    "Java Final Class Type Protected Member",
    "Java Final Class Type Public Member",
    "Java Interface Type Default",
    "Java Interface Type Private",
    "Java Interface Type Protected",
    "Java Interface Type Public",
    "Java Static Abstract Class Type Default Member",
    "Java Static Abstract Class Type Private Member",
    "Java Static Abstract Class Type Protected Member",
    "Java Static Abstract Class Type Public Member",
    "Java Static Class Type Default Member",
    "Java Static Class Type Private Member",
    "Java Static Class Type Protected Member",
    "Java Static Class Type Public Member",
    "Java Static Final Class Type Default Member",
    "Java Static Final Class Type Private Member",
    "Java Static Final Class Type Protected Member",
    "Java Static Final Class Type Public Member",
    "Java Class Type TypeVariable",
    "Java Unknown Class Type Member",
    "Java Unresolved Type",
  },
  "Unused": {
    "Java Unused",
  },
  "Variable": {
    "Java Variable EnumConstant Public Member",
    "Java Final Variable Default Member",
    "Java Final Variable Local",
    "Java Final Variable Private Member",
    "Java Final Variable Protected Member",
    "Java Final Variable Public Member",
    "Java Static Final Variable Default Member",
    "Java Static Final Variable Private Member",
    "Java Static Final Variable Protected Member",
    "Java Static Final Variable Public Member",
    "Java Static Variable Default Member",
    "Java Static Variable Private Member",
    "Java Static Variable Protected Member",
    "Java Static Variable Public Member",
    "Java Unknown Variable Member",
    "Java Unresolved Variable",
    "Java Variable Default Member",
    "Java Variable Local",
    "Java Variable Private Member",
    "Java Variable Protected Member",
    "Java Variable Public Member",
  },
}

RefMap = {
  "Call": {
    "Java Call",
    "Java Call Nondynamic",
  },
  "Cast": {
    "Java Cast",
  },
  "Contain": {
    "Java Contain",
  },
  "Couple": {
    "Java Couple",
    "Java Extend Couple",
    "Java Extend Couple External",
    "Java Extend Couple Implicit External",
    "Java Extend Couple Implicit",
    "Java Implement Couple",
  },
  "Create": {
    "Java Create",
  },
  "Define": {
    "Java Define",
  },
  "DotRef": {
    "Java DotRef",
  },
  "End": {
    "Java End",
  },
  "Import": {
    "Java Import",
    "Java Import Demand",
  },
  "Modify": {
    "Java Modify",
  },
  "Override": {
    "Java Override",
  },
  "Set": {
    "Java Set",
    "Java Set Init",
    "Java Set Partial",
  },
  "Typed": {
    "Java Typed",
  },
  "Use": {
    "Java Use",
    "Java Use Partial",
  },
  "Throw": {
    "Java Throw",
  },
}


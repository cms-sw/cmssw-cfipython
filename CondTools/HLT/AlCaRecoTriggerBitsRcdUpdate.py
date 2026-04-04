import FWCore.ParameterSet.Config as cms

def AlCaRecoTriggerBitsRcdUpdate(*args, **kwargs):
  mod = cms.EDAnalyzer('AlCaRecoTriggerBitsRcdUpdate',
    firstRunIOV = cms.uint32(1),
    lastRunIOV = cms.int32(-1),
    startEmpty = cms.bool(True),
    listNamesRemove = cms.vstring(),
    triggerListsAdd = cms.VPSet(
      template = cms.PSetTemplate(
        listName = cms.required.string,
        hltPaths = cms.required.vstring
      )
    ),
    alcarecoToReplace = cms.VPSet(
      template = cms.PSetTemplate(
        oldKey = cms.required.string,
        newKey = cms.required.string
      )
    ),
    pathsToAdd = cms.VPSet(
      template = cms.PSetTemplate(
        listName = cms.required.string,
        hltPaths = cms.required.vstring
      )
    ),
    pathsToRemove = cms.VPSet(
      template = cms.PSetTemplate(
        listName = cms.required.string,
        hltPaths = cms.required.vstring
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

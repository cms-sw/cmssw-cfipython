import FWCore.ParameterSet.Config as cms

def AlCaRecoTriggerBitsRcdUpdate(*args, **kwargs):
  mod = cms.EDAnalyzer('AlCaRecoTriggerBitsRcdUpdate',
    firstRunIOV = cms.uint32(1),
    lastRunIOV = cms.int32(-1),
    startEmpty = cms.bool(True),
    listNamesRemove = cms.vstring(),
    triggerListsAdd = cms.VPSet(
    ),
    alcarecoToReplace = cms.VPSet(
    ),
    pathsToAdd = cms.VPSet(
    ),
    pathsToRemove = cms.VPSet(
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

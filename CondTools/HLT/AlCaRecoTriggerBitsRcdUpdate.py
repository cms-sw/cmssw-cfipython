import FWCore.ParameterSet.Config as cms

def AlCaRecoTriggerBitsRcdUpdate(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

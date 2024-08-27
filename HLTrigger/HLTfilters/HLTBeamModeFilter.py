import FWCore.ParameterSet.Config as cms

def HLTBeamModeFilter(**kwargs):
  mod = cms.EDFilter('HLTBeamModeFilter',
    saveTags = cms.bool(True),
    L1GtEvmReadoutRecordTag = cms.InputTag('gtEvmDigis'),
    AllowedBeamMode = cms.vuint32(11),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

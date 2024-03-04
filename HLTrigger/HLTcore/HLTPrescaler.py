import FWCore.ParameterSet.Config as cms

def HLTPrescaler(**kwargs):
  mod = cms.EDFilter('HLTPrescaler',
    offset = cms.uint32(0),
    L1GtReadoutRecordTag = cms.InputTag('hltGtStage2Digis'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def HLTPrescaler(*args, **kwargs):
  mod = cms.EDFilter('HLTPrescaler',
    offset = cms.uint32(0),
    L1GtReadoutRecordTag = cms.InputTag('hltGtStage2Digis'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def PatFromScoutingMuonProducer(*args, **kwargs):
  mod = cms.EDProducer('PatFromScoutingMuonProducer',
    src = cms.InputTag('hltScoutingMuonPacker'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

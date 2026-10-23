import FWCore.ParameterSet.Config as cms

def MuonShowerInformationProducer(*args, **kwargs):
  mod = cms.EDProducer('MuonShowerInformationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

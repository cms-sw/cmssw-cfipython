import FWCore.ParameterSet.Config as cms

def MuonLinksProducer(*args, **kwargs):
  mod = cms.EDProducer('MuonLinksProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

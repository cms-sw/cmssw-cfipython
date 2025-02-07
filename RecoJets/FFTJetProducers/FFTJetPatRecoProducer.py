import FWCore.ParameterSet.Config as cms

def FFTJetPatRecoProducer(*args, **kwargs):
  mod = cms.EDProducer('FFTJetPatRecoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

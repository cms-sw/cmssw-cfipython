import FWCore.ParameterSet.Config as cms

def FFTJetPatRecoProducer(**kwargs):
  mod = cms.EDProducer('FFTJetPatRecoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

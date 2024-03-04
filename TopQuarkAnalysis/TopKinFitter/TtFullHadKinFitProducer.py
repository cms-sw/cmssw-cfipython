import FWCore.ParameterSet.Config as cms

def TtFullHadKinFitProducer(**kwargs):
  mod = cms.EDProducer('TtFullHadKinFitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

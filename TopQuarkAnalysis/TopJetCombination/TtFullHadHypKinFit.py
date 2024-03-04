import FWCore.ParameterSet.Config as cms

def TtFullHadHypKinFit(**kwargs):
  mod = cms.EDProducer('TtFullHadHypKinFit',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

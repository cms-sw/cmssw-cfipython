import FWCore.ParameterSet.Config as cms

def TtSemiLepKinFitProducerMuon(**kwargs):
  mod = cms.EDProducer('TtSemiLepKinFitProducerMuon',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

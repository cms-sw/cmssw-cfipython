import FWCore.ParameterSet.Config as cms

def DataCertificationJetMET(**kwargs):
  mod = cms.EDProducer('DataCertificationJetMET',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

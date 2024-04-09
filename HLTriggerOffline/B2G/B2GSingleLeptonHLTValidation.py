import FWCore.ParameterSet.Config as cms

def B2GSingleLeptonHLTValidation(**kwargs):
  mod = cms.EDProducer('B2GSingleLeptonHLTValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
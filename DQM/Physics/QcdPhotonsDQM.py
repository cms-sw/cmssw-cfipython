import FWCore.ParameterSet.Config as cms

def QcdPhotonsDQM(**kwargs):
  mod = cms.EDProducer('QcdPhotonsDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

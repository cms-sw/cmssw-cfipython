import FWCore.ParameterSet.Config as cms

def TransientIntProducerEndProcessBlock(**kwargs):
  mod = cms.EDProducer('TransientIntProducerEndProcessBlock',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

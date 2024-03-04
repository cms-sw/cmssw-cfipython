import FWCore.ParameterSet.Config as cms

def EcalPhiSymInfoFlatTableProducerRun(**kwargs):
  mod = cms.EDProducer('EcalPhiSymInfoFlatTableProducerRun',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def EcalPhiSymInfoFlatTableProducerRun(*args, **kwargs):
  mod = cms.EDProducer('EcalPhiSymInfoFlatTableProducerRun',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

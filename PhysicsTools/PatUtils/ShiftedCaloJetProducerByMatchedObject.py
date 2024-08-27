import FWCore.ParameterSet.Config as cms

def ShiftedCaloJetProducerByMatchedObject(**kwargs):
  mod = cms.EDProducer('ShiftedCaloJetProducerByMatchedObject',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

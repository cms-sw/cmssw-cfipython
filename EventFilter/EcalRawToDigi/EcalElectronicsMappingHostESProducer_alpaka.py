import FWCore.ParameterSet.Config as cms

def EcalElectronicsMappingHostESProducer_alpaka(**kwargs):
  mod = cms.ESProducer('EcalElectronicsMappingHostESProducer@alpaka',
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

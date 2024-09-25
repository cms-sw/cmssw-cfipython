import FWCore.ParameterSet.Config as cms

def EcalElectronicsMappingHostESProducer_alpaka(*args, **kwargs):
  mod = cms.ESProducer('EcalElectronicsMappingHostESProducer@alpaka',
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

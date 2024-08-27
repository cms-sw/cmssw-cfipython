import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_EcalMultifitConditionsHostESProducer(**kwargs):
  mod = cms.ESProducer('alpaka_rocm_async::EcalMultifitConditionsHostESProducer',
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

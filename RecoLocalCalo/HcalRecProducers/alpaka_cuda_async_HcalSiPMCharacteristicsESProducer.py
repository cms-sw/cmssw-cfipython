import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_HcalSiPMCharacteristicsESProducer(**kwargs):
  mod = cms.ESProducer('alpaka_cuda_async::HcalSiPMCharacteristicsESProducer',
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

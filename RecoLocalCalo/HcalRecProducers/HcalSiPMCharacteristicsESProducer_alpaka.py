import FWCore.ParameterSet.Config as cms

def HcalSiPMCharacteristicsESProducer_alpaka(**kwargs):
  mod = cms.ESProducer('HcalSiPMCharacteristicsESProducer@alpaka',
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
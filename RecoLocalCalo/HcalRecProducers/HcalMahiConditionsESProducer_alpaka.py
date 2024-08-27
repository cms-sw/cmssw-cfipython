import FWCore.ParameterSet.Config as cms

def HcalMahiConditionsESProducer_alpaka(**kwargs):
  mod = cms.ESProducer('HcalMahiConditionsESProducer@alpaka',
    appendToDataLabel = cms.string(''),
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def EcalPhase2DigiToGPUProducer(**kwargs):
  mod = cms.EDProducer('EcalPhase2DigiToGPUProducer',
    BarrelDigis = cms.InputTag('simEcalUnsuppressedDigis'),
    digisLabelEB = cms.string('ebDigis'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

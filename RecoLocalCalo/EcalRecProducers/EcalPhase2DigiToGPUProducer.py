import FWCore.ParameterSet.Config as cms

def EcalPhase2DigiToGPUProducer(*args, **kwargs):
  mod = cms.EDProducer('EcalPhase2DigiToGPUProducer',
    BarrelDigis = cms.InputTag('simEcalUnsuppressedDigis'),
    digisLabelEB = cms.string('ebDigis'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

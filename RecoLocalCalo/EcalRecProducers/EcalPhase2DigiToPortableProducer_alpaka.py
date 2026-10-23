import FWCore.ParameterSet.Config as cms

def EcalPhase2DigiToPortableProducer_alpaka(*args, **kwargs):
  mod = cms.EDProducer('EcalPhase2DigiToPortableProducer@alpaka',
    BarrelDigis = cms.InputTag('simEcalUnsuppressedDigis'),
    digisLabelEB = cms.string('ebDigis'),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string(''),
      synchronize = cms.optional.untracked.bool
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

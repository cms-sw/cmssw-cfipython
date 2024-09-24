import FWCore.ParameterSet.Config as cms

def PatJetIDValueMapProducer(*args, **kwargs):
  mod = cms.EDProducer('PatJetIDValueMapProducer',
    src = cms.required.InputTag,
    filterParams = cms.PSet(
      version = cms.string('RUN3PUPPIruns2022FGruns2023CD'),
      quality = cms.string('TIGHT'),
      cutsToIgnore = cms.optional.vstring
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

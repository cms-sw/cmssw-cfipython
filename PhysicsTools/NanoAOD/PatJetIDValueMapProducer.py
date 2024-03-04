import FWCore.ParameterSet.Config as cms

def PatJetIDValueMapProducer(**kwargs):
  mod = cms.EDProducer('PatJetIDValueMapProducer',
    src = cms.required.InputTag,
    filterParams = cms.PSet(
      version = cms.string('RUN3PUPPIruns2022FGruns2023CD'),
      quality = cms.string('TIGHT'),
      cutsToIgnore = cms.optional.vstring
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

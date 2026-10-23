import FWCore.ParameterSet.Config as cms

def PFJetIDSelectionFunctorFilter(*args, **kwargs):
  mod = cms.EDFilter('PFJetIDSelectionFunctorFilter',
    src = cms.InputTag(''),
    filterParams = cms.PSet(
      version = cms.string('RUN3PUPPIruns2022FGruns2023CD'),
      quality = cms.string('TIGHT'),
      cutsToIgnore = cms.optional.vstring
    ),
    filter = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

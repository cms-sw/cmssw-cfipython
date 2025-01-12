import FWCore.ParameterSet.Config as cms

def JetIDSelectionFunctorFilter(*args, **kwargs):
  mod = cms.EDFilter('JetIDSelectionFunctorFilter',
    src = cms.InputTag(''),
    filterParams = cms.PSet(
      version = cms.string(''),
      quality = cms.string('')
    ),
    filter = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

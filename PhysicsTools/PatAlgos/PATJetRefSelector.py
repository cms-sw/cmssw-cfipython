import FWCore.ParameterSet.Config as cms

def PATJetRefSelector(*args, **kwargs):
  mod = cms.EDFilter('PATJetRefSelector',
    src = cms.InputTag(''),
    cut = cms.string(''),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

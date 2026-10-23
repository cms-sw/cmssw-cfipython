import FWCore.ParameterSet.Config as cms

def PATJetSelector(*args, **kwargs):
  mod = cms.EDFilter('PATJetSelector',
    src = cms.InputTag('no default'),
    cut = cms.string(''),
    cutLoose = cms.string(''),
    filter = cms.bool(False),
    nLoose = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

import FWCore.ParameterSet.Config as cms

def PATJetSelector(**kwargs):
  mod = cms.EDFilter('PATJetSelector',
    src = cms.InputTag('no default'),
    cut = cms.string(''),
    cutLoose = cms.string(''),
    filter = cms.bool(False),
    nLoose = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

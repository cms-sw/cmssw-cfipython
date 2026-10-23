import FWCore.ParameterSet.Config as cms

def MuonRefPatCount(*args, **kwargs):
  mod = cms.EDFilter('MuonRefPatCount',
    src = cms.InputTag(''),
    cut = cms.string(''),
    minNumber = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

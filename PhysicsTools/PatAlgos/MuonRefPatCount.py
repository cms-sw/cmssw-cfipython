import FWCore.ParameterSet.Config as cms

def MuonRefPatCount(**kwargs):
  mod = cms.EDFilter('MuonRefPatCount',
    src = cms.InputTag(''),
    cut = cms.string(''),
    minNumber = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

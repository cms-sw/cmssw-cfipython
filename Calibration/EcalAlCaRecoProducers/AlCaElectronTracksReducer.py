import FWCore.ParameterSet.Config as cms

def AlCaElectronTracksReducer(**kwargs):
  mod = cms.EDProducer('AlCaElectronTracksReducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

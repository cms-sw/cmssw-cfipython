import FWCore.ParameterSet.Config as cms

def XangleBetaStarFilter(*args, **kwargs):
  mod = cms.EDFilter('XangleBetaStarFilter',
    lhcInfoLabel = cms.string(''),
    lhcInfoPerLSLabel = cms.string(''),
    lhcInfoPerFillLabel = cms.string(''),
    useNewLHCInfo = cms.bool(False),
    xangle_min = cms.double(0),
    xangle_max = cms.double(1000),
    beta_star_min = cms.double(0),
    beta_star_max = cms.double(1000),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

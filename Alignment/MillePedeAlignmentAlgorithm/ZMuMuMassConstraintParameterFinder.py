import FWCore.ParameterSet.Config as cms

def ZMuMuMassConstraintParameterFinder(*args, **kwargs):
  mod = cms.EDAnalyzer('ZMuMuMassConstraintParameterFinder',
    pMin = cms.double(3),
    ptMin = cms.double(15),
    etaMin = cms.double(-3),
    etaMax = cms.double(3),
    phiMin = cms.double(-3.1415926535897931),
    phiMax = cms.double(3.1415926535897931),
    minMassPair = cms.double(85.8),
    maxMassPair = cms.double(95.8),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

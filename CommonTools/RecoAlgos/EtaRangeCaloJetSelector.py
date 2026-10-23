import FWCore.ParameterSet.Config as cms

def EtaRangeCaloJetSelector(*args, **kwargs):
  mod = cms.EDFilter('EtaRangeCaloJetSelector',
    src = cms.InputTag(''),
    etaMin = cms.double(0),
    etaMax = cms.double(0),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

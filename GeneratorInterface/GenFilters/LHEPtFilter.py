import FWCore.ParameterSet.Config as cms

def LHEPtFilter(*args, **kwargs):
  mod = cms.EDFilter('LHEPtFilter',
    selectedPdgIds = cms.vint32(),
    ptMin = cms.double(0),
    ptMax = cms.double(-1),
    isScalar = cms.bool(False),
    src = cms.InputTag('externalLHEProducer'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

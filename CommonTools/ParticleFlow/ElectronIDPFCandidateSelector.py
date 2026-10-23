import FWCore.ParameterSet.Config as cms

def ElectronIDPFCandidateSelector(*args, **kwargs):
  mod = cms.EDFilter('ElectronIDPFCandidateSelector',
    src = cms.InputTag(''),
    recoGsfElectrons = cms.InputTag(''),
    electronIdMap = cms.InputTag(''),
    electronIdCut = cms.double(0),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

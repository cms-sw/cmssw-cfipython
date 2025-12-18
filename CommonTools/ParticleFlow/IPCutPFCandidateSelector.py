import FWCore.ParameterSet.Config as cms

def IPCutPFCandidateSelector(*args, **kwargs):
  mod = cms.EDFilter('IPCutPFCandidateSelector',
    src = cms.InputTag(''),
    vertices = cms.InputTag(''),
    d0Cut = cms.double(0.2),
    dzCut = cms.double(0.5),
    dtCut = cms.double(-1),
    d0SigCut = cms.double(99),
    dzSigCut = cms.double(99),
    dtSigCut = cms.double(-1),
    filter = cms.bool(False),
    throwOnMissing = cms.untracked.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

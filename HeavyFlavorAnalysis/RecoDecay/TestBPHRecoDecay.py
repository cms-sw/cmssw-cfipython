import FWCore.ParameterSet.Config as cms

def TestBPHRecoDecay(*args, **kwargs):
  mod = cms.EDAnalyzer('TestBPHRecoDecay',
    patMuonLabel = cms.string(''),
    ccCandsLabel = cms.string(''),
    pfCandsLabel = cms.string(''),
    pcCandsLabel = cms.string(''),
    gpCandsLabel = cms.string(''),
    outDump = cms.string('dump.txt'),
    outHist = cms.string('hist.root'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod

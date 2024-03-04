import FWCore.ParameterSet.Config as cms

def TestBPHRecoDecay(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

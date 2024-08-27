import FWCore.ParameterSet.Config as cms

def BPHHistoSpecificDecay(**kwargs):
  mod = cms.EDAnalyzer('BPHHistoSpecificDecay',
    trigResultsLabel = cms.string(''),
    oniaCandsLabel = cms.string(''),
    sdCandsLabel = cms.string(''),
    ssCandsLabel = cms.string(''),
    buCandsLabel = cms.string(''),
    bdCandsLabel = cms.string(''),
    bsCandsLabel = cms.string(''),
    k0CandsLabel = cms.string(''),
    l0CandsLabel = cms.string(''),
    b0CandsLabel = cms.string(''),
    lbCandsLabel = cms.string(''),
    bcCandsLabel = cms.string(''),
    x3872CandsLabel = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

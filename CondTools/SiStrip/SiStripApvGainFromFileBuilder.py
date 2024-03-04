import FWCore.ParameterSet.Config as cms

def SiStripApvGainFromFileBuilder(**kwargs):
  mod = cms.EDAnalyzer('SiStripApvGainFromFileBuilder',
    tickFile = cms.FileInPath('CondTools/SiStrip/data/tickheight.txt'),
    gainThreshold = cms.double(0),
    dummyAPVGain = cms.double(1.078125),
    doGainNormalization = cms.bool(False),
    putDummyIntoUncabled = cms.bool(False),
    putDummyIntoUnscanned = cms.bool(False),
    putDummyIntoOffChannels = cms.bool(False),
    putDummyIntoBadChannels = cms.bool(False),
    outputMaps = cms.bool(False),
    outputSummary = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod

import FWCore.ParameterSet.Config as cms

def L1CTJetFileWriter(**kwargs):
  mod = cms.EDAnalyzer('L1CTJetFileWriter',
    collections = cms.required.VPSet,
    outputFilename = cms.required.string,
    outputFileExtension = cms.string('txt'),
    nJets = cms.uint32(12),
    nFramesPerBX = cms.uint32(9),
    gapLengthOutput = cms.uint32(4),
    TMUX = cms.uint32(6),
    maxLinesPerFile = cms.uint32(1024),
    format = cms.string('EMPv2'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
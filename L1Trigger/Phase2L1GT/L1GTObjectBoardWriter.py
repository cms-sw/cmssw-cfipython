import FWCore.ParameterSet.Config as cms

def L1GTObjectBoardWriter(**kwargs):
  mod = cms.EDAnalyzer('L1GTObjectBoardWriter',
    filename = cms.required.untracked.string,
    fileExtension = cms.untracked.string('txt'),
    maxFrames = cms.untracked.uint32(1024),
    maxEvents = cms.untracked.uint32(0),
    patternFormat = cms.untracked.string('EMPv2'),
    bufferFileType = cms.untracked.string('input'),
    GTTPromptJets = cms.required.untracked.InputTag,
    GTTDisplacedJets = cms.required.untracked.InputTag,
    GTTPromptHtSum = cms.required.untracked.InputTag,
    GTTDisplacedHtSum = cms.required.untracked.InputTag,
    GTTEtSum = cms.required.untracked.InputTag,
    GTTPrimaryVert = cms.required.untracked.InputTag,
    GMTSaPromptMuons = cms.required.untracked.InputTag,
    GMTSaDisplacedMuons = cms.required.untracked.InputTag,
    GMTTkMuons = cms.required.untracked.InputTag,
    CL2JetsSC4 = cms.required.untracked.InputTag,
    CL2JetsSC8 = cms.required.untracked.InputTag,
    CL2Photons = cms.required.untracked.InputTag,
    CL2Electrons = cms.required.untracked.InputTag,
    CL2Taus = cms.required.untracked.InputTag,
    CL2EtSum = cms.required.untracked.InputTag,
    CL2HtSum = cms.required.untracked.InputTag,
    InputChannels = cms.untracked.PSet(
      GCT_1 = cms.required.untracked.vuint32,
      GMT_1 = cms.required.untracked.vuint32,
      GTT_1 = cms.required.untracked.vuint32,
      GTT_2 = cms.required.untracked.vuint32,
      GTT_3 = cms.required.untracked.vuint32,
      GTT_4 = cms.required.untracked.vuint32,
      CL2_1 = cms.required.untracked.vuint32,
      CL2_2 = cms.required.untracked.vuint32,
      CL2_3 = cms.required.untracked.vuint32
    ),
    OutputChannels = cms.untracked.PSet(
      GTTPromptJets = cms.required.untracked.vuint32,
      GTTDisplacedJets = cms.required.untracked.vuint32,
      GTTPromptHtSum = cms.required.untracked.vuint32,
      GTTDisplacedHtSum = cms.required.untracked.vuint32,
      GTTEtSum = cms.required.untracked.vuint32,
      GTTHadronicTaus = cms.required.untracked.vuint32,
      CL2JetsSC4 = cms.required.untracked.vuint32,
      CL2JetsSC8 = cms.required.untracked.vuint32,
      CL2Taus = cms.required.untracked.vuint32,
      CL2HtSum = cms.required.untracked.vuint32,
      CL2EtSum = cms.required.untracked.vuint32,
      GCTNonIsoEg = cms.required.untracked.vuint32,
      GCTIsoEg = cms.required.untracked.vuint32,
      GCTJets = cms.required.untracked.vuint32,
      GCTTaus = cms.required.untracked.vuint32,
      GCTHtSum = cms.required.untracked.vuint32,
      GCTEtSum = cms.required.untracked.vuint32,
      GMTSaPromptMuons = cms.required.untracked.vuint32,
      GMTSaDisplacedMuons = cms.required.untracked.vuint32,
      GMTTkMuons = cms.required.untracked.vuint32,
      GMTTopo = cms.required.untracked.vuint32,
      CL2Electrons = cms.required.untracked.vuint32,
      CL2Photons = cms.required.untracked.vuint32,
      GTTPhiCandidates = cms.required.untracked.vuint32,
      GTTRhoCandidates = cms.required.untracked.vuint32,
      GTTBsCandidates = cms.required.untracked.vuint32,
      GTTPrimaryVert = cms.required.untracked.vuint32
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
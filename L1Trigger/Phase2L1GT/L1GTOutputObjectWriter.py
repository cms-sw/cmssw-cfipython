import FWCore.ParameterSet.Config as cms

def L1GTOutputObjectWriter(**kwargs):
  mod = cms.EDAnalyzer('L1GTOutputObjectWriter',
    GCTNonIsoEg = cms.required.InputTag,
    GCTIsoEg = cms.required.InputTag,
    GCTJets = cms.required.InputTag,
    GCTTaus = cms.required.InputTag,
    GCTHtSum = cms.required.InputTag,
    GCTEtSum = cms.required.InputTag,
    GMTSaPromptMuons = cms.required.InputTag,
    GMTSaDisplacedMuons = cms.required.InputTag,
    GMTTkMuons = cms.required.InputTag,
    GMTTopo = cms.required.InputTag,
    GTTPromptJets = cms.required.InputTag,
    GTTDisplacedJets = cms.required.InputTag,
    GTTPhiCandidates = cms.required.InputTag,
    GTTRhoCandidates = cms.required.InputTag,
    GTTBsCandidates = cms.required.InputTag,
    GTTHadronicTaus = cms.required.InputTag,
    GTTPrimaryVert = cms.required.InputTag,
    GTTPromptHtSum = cms.required.InputTag,
    GTTDisplacedHtSum = cms.required.InputTag,
    GTTEtSum = cms.required.InputTag,
    CL2JetsSC4 = cms.required.InputTag,
    CL2JetsSC8 = cms.required.InputTag,
    CL2Taus = cms.required.InputTag,
    CL2Electrons = cms.required.InputTag,
    CL2Photons = cms.required.InputTag,
    CL2HtSum = cms.required.InputTag,
    CL2EtSum = cms.required.InputTag,
    maxLines = cms.uint32(1024),
    outputFilename = cms.required.string,
    outputFileExtension = cms.string('txt'),
    patternFormat = cms.string('EMPv2'),
    platform = cms.string('VU9P'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
